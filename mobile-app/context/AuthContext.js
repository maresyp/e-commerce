import { createContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode"
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from "react-native";
import { decode as atob, encode as btoa } from 'base-64'

if (!global.btoa) {
    global.btoa = btoa;
}

if (!global.atob) {
    global.atob = atob;
}

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({ children }) => {
    // Get auth token and user from local storage if possible else null
    let [authTokens, setAuthTokens] = useState(null);
    let [user, setUser] = useState(null)
    let [loading, setLoading] = useState(true)

    const navigation = useNavigation()
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';

    useEffect(() => {
        const fetchTokens = async () => {
            const tokens = await AsyncStorage.getItem('authTokens');
            tokens ? setAuthTokens(JSON.parse(tokens)) : null;
        }

        const fetchUser = async () => {
            const tokens = await AsyncStorage.getItem('authTokens');
            tokens ? setUser(jwtDecode(await AsyncStorage.getItem('authTokens'))) : null;
        }

        fetchTokens();
        fetchUser();
    }, [])

    let updateToken = async () => {
        console.log("Trying to update token");
        await fetch(
            `${apiUrl}token/refresh/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'refresh': authTokens?.refresh })
        }).then(res => {
            if (!res.ok) {
                clearUserData()
                throw new Error('Failed to fetch, status=' + res.status)
            }
            return res.json()
        }).then(d => {
            console.log(d);
            setAuthTokens(d)
            setUser(jwtDecode(d.access))
            AsyncStorage.setItem('authTokens', JSON.stringify(d))
        }).catch(e => {
            console.log("updateToken " + e);
        }).finally(() => {
            if (loading) {
                setLoading(false)
            }
        })
    }

    let loginUser = async (login, pwd) => {
        let response = await fetch(
            `${apiUrl}token/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'username': login, 'password': pwd })
        })

        const data = await response.json();

        if (response.status === 200) {
            setAuthTokens(data)
            setUser(jwtDecode(data.access))
            await AsyncStorage.setItem('authTokens', JSON.stringify(data))
            navigation.navigate('/')
            return true
        } else {
            return false
            // TODO: This need error handling ( network errors )
        }
    }

    const clearUserData = async () => {
        setAuthTokens(null)
        setUser(null)
        await AsyncStorage.removeItem('authTokens')
    }

    let logoutUser = () => {
        clearUserData()
        navigation.navigate('/')
    }

    let contextData = {
        user: user,
        authTokens: authTokens,
        loginUser: loginUser,
        logoutUser: logoutUser,
    }

    useEffect(() => {

        if (loading) {
            updateToken()
        }

        let fourMinutes = 1000 * 60 * 4
        let interval = setInterval(() => {
            if (authTokens) {
                updateToken()
            }
        }, fourMinutes)
        return () => clearInterval(interval)

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData}>
            {loading ? null : children}
        </AuthContext.Provider>
    )
}