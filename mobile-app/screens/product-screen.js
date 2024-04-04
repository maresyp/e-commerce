import React, { useCallback, useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, FlatList, TouchableOpacity, Platform } from 'react-native';
import axios from 'axios';
import Toast from 'react-native-toast-message';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { ScrollView, TextInput } from 'react-native-gesture-handler';
import { useFocusEffect } from '@react-navigation/native';

const ProductScreen = ({ route }) => {
    const { productId } = route.params;
    const [product, setProduct] = useState(null);
    const [cartId, setCartId] = useState(null);
    const [quantity, setQuantity] = useState(1);
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';
    
    const getImageUrl = (productId) => `${apiUrl}get_product_image/${productId}`;
    
    const fetchProductData = async (productId) => {
        try {
            const response = await axios.get(`${apiUrl}get_single_product/${productId}`);
            setProduct(response.data); // Ustawienie danych produktu w stanie
        } catch (error) {
            console.error('Błąd podczas pobierania danych produktu:', error);
        }
    };

    useFocusEffect(
        useCallback(() => {
            const fetchCartId = async () => {
                try {
                    const storedCartId = await AsyncStorage.getItem('cart_id');
                    if (storedCartId !== null) {
                        setCartId(storedCartId);
                        fetchProductData(productId);
                    }
                } catch (error) {
                    console.error('Błąd podczas odczytu cart_id z AsyncStorage:', error);
                }
            };


            fetchCartId();
        }, [])
    );

    const addToCart = (productId, amount) => {
        if (!cartId) {
            console.error("Dane koszyka nie są jeszcze dostępne");
            return;
        }

        const data = {
            amount: amount,
            product_id: productId,
            cart_id: cartId,
        };

        axios.post(`${apiUrl}cart_add_product/`, data, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(() => {
            console.log("Dodano produkt ", productId, "do koszyka: ", cartId);

            Toast.show({
                type: 'success',
                position: 'top',
                text1: 'Dodano produkt do koszyka.',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
              });
        })
        .catch(error => {
            console.error("Wystąpił błąd przy dodawaniu do koszyka: ", error);
            Toast.show({
                type: 'error',
                position: 'top',
                text1: 'Wystąpił błąd przy dodawaniu do koszyka.',
                visibilityTime: 4000,
                autoHide: true,
                topOffset: 120,
                bottomOffset: 40,
              });
        });
    };

    return (
        <ScrollView style={styles.product}>
            {product && ( // Warunkowe renderowanie - sprawdzenie, czy product nie jest null
                <>
                    <View style={styles.infoFirst}>
                        <Image
                            style={styles.productImage}
                            source={{ uri: getImageUrl(productId) }}
                        />
                        <Text style={styles.productName}>{product.name}</Text>
                    </View>

                    <Text style={styles.productDescriptionTitle}>Opis produktu:</Text>
                    <Text style={styles.productDescription}>{product.description}</Text>

                    <View style={styles.infoSecond}>
                        <Text style={styles.productQuantity}>Ilość: </Text>
                        <TextInput
                            style={styles.input}
                            onChangeText={text => {
                                const value = parseInt(text);
                                if (!isNaN(value) && value >= 1 && value <= 100) {
                                    setQuantity(value);
                                }
                            }}
                            value={quantity.toString()}
                            keyboardType="numeric"
                        />
                    </View>

                    <TouchableOpacity style={styles.addButton} onPress={() => addToCart(product.id, quantity)}>
                        <Text style={styles.buttonText}>Dodaj do koszyka</Text>
                    </TouchableOpacity>
                </>
            )}
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    product: {
        marginHorizontal: '2.5%',
        marginVertical: '1%',
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
        width: '95',
    },
    infoFirst: {
        flexDirection: 'row',
        justifyContent: 'flex-start',
        alignItems: 'center',
        margin: 10,
    },
    infoSecond: {
        alignSelf:'flex-end',
        flexDirection: 'row',
        justifyContent: 'flex-end',
        alignItems: 'center',
        marginTop: 20,
    },
    productName: {
        fontSize: 25,
        fontWeight: 'bold',
        marginLeft: 20,
    },
    productDescriptionTitle: {
        fontSize: 22,
        fontWeight: 'bold',
        margin: 10,
    },
    productDescription: {
        marginHorizontal: 10, 
    },
    productImage: {
        width: 150,
        height: 150,
        borderRadius: 75,
        borderWidth: 3,
        borderColor: '#299ad7',
    },
    productPrice: {
        fontSize: 16,
        fontWeight: 'bold',
        margin: 5,
    },
    addButton: {
        backgroundColor: '#299ad7',
        margin: 2,
        borderRadius: 10,
        padding: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.9,
        shadowRadius: 2,
        elevation: 5,
    },
    buttonText: {
        color: 'white',
        fontSize: 20,
        textAlign: 'center',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        borderRadius: 10,
        marginBottom: 10,
        paddingHorizontal: 10,
        width: '20%',
        textAlign: 'center',
        alignSelf: 'flex-end',
        fontSize: 20,
    },
    productQuantity: {
        fontSize: 20,
        textAlign: 'center',
        textAlignVertical: 'center',
    }
});

export default ProductScreen;