import React, { useCallback, useContext, useState } from 'react';
import { View, Text, Image, StyleSheet, FlatList, TouchableOpacity, Platform } from 'react-native';
import axios from 'axios';
import Toast from 'react-native-toast-message';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { ScrollView, TextInput } from 'react-native-gesture-handler';
import { useFocusEffect } from '@react-navigation/native';
import { useNavigation } from '@react-navigation/native';
import AuthContext from '../context/AuthContext';

const AccountScreen = () => {
    const [isLoading, setIsLoading] = useState(true);
    const { user, authTokens } = useContext(AuthContext);
    const [adressFormData, setAdressFormData] = useState({
        city: '',
        street: '',
        house_number: '',
        postal_code: '',
        phone_number: '',
        shopping_cart_id:''
    });
    const [pwdFormData, setPwdFormData] = useState({
        old_password: '',
        new_password: '',
        confirm_password: '',
    });
    const navigation = useNavigation();
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';
    let { logoutUser } = useContext(AuthContext);

    useFocusEffect(
        useCallback(() => {
        }, [])
    );

    const handleAdressInputChange = (key, value) => {
        setAdressFormData({
            ...adressFormData,
            [key]: value
        });
    };

    const handlePwdInputChange = (key, value) => {
        setPwdFormData({
            ...pwdFormData,
            [key]: value
        });
    };

    const handleLogoutSubmit = async () => {
        let result = await logoutUser()
        if (result) {
            Toast.show({
                type: 'success',
                position: 'top',
                text1: 'Pomyślnie wylogowano!',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
              });
            navigation.navigate("Home");
        }
        else
        {
            Toast.show({
                type: 'error',
                position: 'top',
                text1: 'Wystąpił nieoczekiwany błąd.',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
              });
        }
    };

    if (false) {
        return (
            <View style={styles.loadingContainer}>
                <Text>Ładowanie zawartości koszyka...</Text>
            </View>
        );
    } 
    else {
        return (
            <ScrollView>
                <View style={styles.adressContainer}>
                    <Text style={styles.sectionTitle}>Adres dostawy</Text>

                    <Text>Miejscowość</Text>
                    <TextInput
                        style={styles.inputField}
                        inputMode='text'
                        keyboardType='default'
                        onChangeText={(text) => handleAdressInputChange('city', text)}
                    />
                    <Text>Ulica</Text>
                    <TextInput
                        style={styles.inputField}
                        inputMode='text'
                        keyboardType='default'
                        onChangeText={(text) => handleAdressInputChange('street', text)}
                    />
                    <Text>Numer domu</Text>
                    <TextInput
                        style={styles.inputField}
                        inputMode='text'
                        keyboardType='default'
                        onChangeText={(text) => handleAdressInputChange('house_number', text)}
                    />
                    <Text>Kod pocztowy</Text>
                    <TextInput
                        style={styles.inputField}
                        inputMode='text'
                        keyboardType='default'
                        onChangeText={(text) => handleAdressInputChange('postal_code', text)}
                    />
                    <Text>Numer telefonu</Text>
                    <TextInput
                        style={styles.inputField}
                        inputMode='tel'
                        keyboardType='phone-pad'
                        onChangeText={(text) => handleAdressInputChange('phone_number', text)}
                    />
                    <TouchableOpacity style={styles.orderButton}>
                        <Text style={styles.buttonText}>Zapisz zmiany</Text>
                    </TouchableOpacity>
                </View>

                <View style={styles.adressContainer}>
                <Text style={styles.sectionTitle}>Zmiana hasła</Text>

                    <Text style={styles.fieldName}>Stare hasło:</Text>
                    <TextInput
                        style={styles.inputField}
                        placeholder="Wprowadź hasło"
                        secureTextEntry
                        onChangeText={(value) => handlePwdInputChange('old_password', value)}
                    />

                    <Text style={styles.fieldName}>Nowe hasło hasło:</Text>
                    <TextInput
                        style={styles.inputField}
                        placeholder="Wprowadź hasło"
                        secureTextEntry
                        onChangeText={(value) => handlePwdInputChange('new_password', value)}
                    />

                    <Text style={styles.fieldName}>Potwierdzenie nowego hasła:</Text>
                    <TextInput
                        style={styles.inputField}
                        placeholder="Potwierdź hasło"
                        secureTextEntry
                        onChangeText={(value) => handlePwdInputChange('confirm_password', value)}
                    />
                    <TouchableOpacity style={styles.orderButton} >
                        <Text style={styles.buttonText}>Zapisz zmiany</Text>
                    </TouchableOpacity>
                </View>

                
                <View style={styles.totalPriceContainer}>
                    <TouchableOpacity style={styles.orderButton} onPress={() => handleLogoutSubmit()}>
                        <Text style={styles.buttonText}>Wyloguj się...</Text>
                    </TouchableOpacity>
                </View>
            </ScrollView>
    );};
};

const styles = StyleSheet.create({
    loadingContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    emptyContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    products: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    flatListContainer: { 
        margin: '2.5%',
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
    },
    totalPriceContainer: {
        marginHorizontal: '2.5%',
        marginBottom: '2.5%',
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
    },
    adressContainer: {
        marginHorizontal: '2.5%',
        marginBottom: '2.5%',
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
    },
    infoFirst: {
        flexDirection: 'row',
        justifyContent: "flex-start",
        alignItems: 'center',
        width: '50%',

    },
    infoSecond: {
        width: '30%',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    infoThird: {
        flexDirection: 'row',
        alignItems: 'center',
        alignSelf: 'flex-end',
        justifyContent: 'space-between',
        width: '30%',
        marginTop: -15,
    },
    productName: {
        fontSize: 25,
        fontWeight: 'bold',
        marginLeft: 10,
    },
    textQuantity: {
        fontSize: 20,
    },
    productImage: {
        width: 50,
        height: 50,
        borderRadius: 25,
        borderWidth: 3,
        borderColor: '#299ad7',
    },
    productQuantity: {
        fontSize: 20,
        fontWeight: 'bold',
        marginLeft: 10,
    },
    line: {
        marginTop: 5,
        marginBottom: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#299ad7',
        width: '90%',
        alignSelf: 'center',
    },
    sectionTitle: {
        fontSize: 25,
        fontWeight: 'bold',
        marginLeft: 10,
        marginBottom: 10,
        alignSelf: 'center',
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
    orderButton: {
        backgroundColor: '#299ad7',
        margin: 10,
        borderRadius: 10,
        padding: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.9,
        shadowRadius: 2,
        elevation: 5,
        alignSelf:'center',
        width: '50%',
    },
    buttonText: {
        fontSize: 20,
        color: 'white',
        textAlign: 'center',
    },
    totalPriceRow: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
});

export default AccountScreen;