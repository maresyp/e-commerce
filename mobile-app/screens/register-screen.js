import { View, Text, StyleSheet, TouchableOpacity, Platform } from 'react-native'
import { useNavigation } from '@react-navigation/native';
import { ScrollView, TextInput } from 'react-native-gesture-handler';
import { useState } from 'react';
import axios from 'axios';
import Toast from 'react-native-toast-message';

const RegisterScreen = () => {
    const navigation = useNavigation();
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';

    const [formData, setFormData] = useState({
        first_name: '',
        username: '',
        email: '',
        password: '',
        pwd2: '',
    })

    const handleInputChange = (name, value) => {
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleRegistration = async () => {
        if (formData['password'] != formData['pwd2']) {
            Toast.show({
                type: 'error',
                position: 'top',
                text1: 'Powtórzone hasło nie jest takie samo.',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
            });

            return
        }

        axios.post(`${apiUrl}register/`, formData, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => {
            console.log("Zarejestrowano: ", response);
            if (response.status === 201) {
                navigation.navigate('Login')
                Toast.show({
                    type: 'success',
                    position: 'top',
                    text1: 'Utworzono konto, zaloguj się',
                    visibilityTime: 4000,
                    autoHide: true,
                    topOffset: 120,
                    bottomOffset: 40,
                });
            }
        }).catch(error => {
            console.error("Wystąpił błąd podczas rejestracji: ", error);
            Toast.show({
                type: 'error',
                position: 'top',
                text1: 'Wystąpił błąd podczas rejestracji.',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
            });
        })
    }

    return (
        <ScrollView style={styles.mainContainer}>
            <Text style={styles.mainText}>Zarejestruj konto</Text>

            <View style={styles.loginForm}>
                <Text style={styles.fieldName}>Imię:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='text'
                    keyboardType='default'
                    placeholder="Podaj swoje imię"
                    onChangeText={(value) => handleInputChange('first_name', value)}
                />

                <Text style={styles.fieldName}>Adres e-mail:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='email'
                    keyboardType='email-address'
                    placeholder="Podaj adres e-mail"
                    onChangeText={(value) => handleInputChange('email', value)}
                />

                <Text style={styles.fieldName}>Nazwa użytkownika:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='text'
                    keyboardType='default'
                    placeholder="Podaj nazwę użytkownika"
                    onChangeText={(value) => handleInputChange('username', value)}
                />

                <Text style={styles.fieldName}>Hasło:</Text>
                <TextInput
                    style={styles.inputField}
                    placeholder="Wprowadź hasło"
                    secureTextEntry
                    onChangeText={(value) => handleInputChange('password', value)}
                />

                <Text style={styles.fieldName}>Potwierdzenie hasła:</Text>
                <TextInput
                    style={styles.inputField}
                    placeholder="Potwierdź hasło"
                    secureTextEntry
                    onChangeText={(value) => handleInputChange('pwd2', value)}
                />

                <TouchableOpacity style={styles.loginBtn} onPress={() => handleRegistration()}>
                    <Text style={styles.buttonText}>Zarejestruj się!</Text>
                </TouchableOpacity>

                <Text style={styles.subText2}>Masz już konto?</Text>
                <TouchableOpacity style={styles.signupBtn} onPress={() => navigation.navigate('Login')}>
                    <Text style={styles.signupText}>Zaloguj się!</Text>
                </TouchableOpacity>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    mainContainer: {
        marginHorizontal: '2.5%',
        marginVertical: '15%',
        paddingVertical: 20,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
        width: '95',
    },
    mainText: {
        fontSize: 30,
        fontWeight: 'bold',
        alignSelf: 'center',
    },
    subText: {
        color: '#949494',
        fontSize: 15,
        alignSelf: 'center',
    },
    subText2: {
        color: '#949494',
        fontSize: 15,
        alignSelf: 'flex-end',
    },
    loginForm: {
        width: '80%',
        alignSelf:  'center',
        marginVertical: 20,
    },
    inputField: {
        backgroundColor: '#d3eaf2',
        borderRadius: 10,
        borderColor: '#e5e7eb',
        borderWidth: 2,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        opacity: 80,
        height: 40,
        marginBottom: 20,
        paddingHorizontal: 10,
    },
    loginBtn: {
        backgroundColor: '#299ad7',
        marginVertical: 20,
        borderRadius: 10,
        padding: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.9,
        shadowRadius: 2,
        elevation: 5,
        width: '80%',
        alignSelf:  'center',
    },
    buttonText: {
        color: 'white',
        fontSize: 20,
        textAlign: 'center',
    },
    signupBtn: {
        alignSelf: 'flex-end',
    },
    signupText: {
        color: '#0051ff',
        fontSize: 15,
    }
});

export default RegisterScreen;