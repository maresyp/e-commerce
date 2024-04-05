import React, { useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, FlatList, TouchableOpacity, Platform, TextInput } from 'react-native';
import axios from 'axios';
import Toast from 'react-native-toast-message';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useNavigation } from '@react-navigation/native';

const HomeScreen = () => {
    const [products, setProducts] = useState([]);
    const [cart, setCart] = useState(null);
    const [searchText, setSearchText] = useState('');
    const navigation = useNavigation();
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';

    // Pobieranie produktów
    useEffect(() => {
        axios.get(`${apiUrl}get_all_products/`)
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    // Pobieranie danych koszyka
    useEffect(() => {
        // Sprawdź, czy w AsyncStorage jest zapisany cart_id
        AsyncStorage.getItem('cart_id')
            .then((cartId) => {
                if (cartId) {
                    // Jeśli jest zapisany, pobierz dane koszyka za pomocą cart_id
                    axios.get(`${apiUrl}cart_get/${cartId}`)
                        .then(response => {
                            setCart(response.data);
                        })
                        .catch(error => {
                            console.error(error);
                        });
                } else {
                    // Jeśli nie ma zapisanego cart_id, pobierz dane koszyka normalnie
                    axios.get(`${apiUrl}cart_get/`)
                        .then(response => {
                            setCart(response.data);
                            AsyncStorage.setItem('cart_id', response.data.cart_id);
                        })
                        .catch(error => {
                            console.error(error);
                        });
                }
            })
            .catch(error => {
                console.error(error);
            });
        
        // Pobieranie produktów
        axios.get(`${apiUrl}get_all_products/`)
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const addToCart = (productId) => {
        if (!cart) {
            console.error("Dane koszyka nie są jeszcze dostępne");
            return;
        }

        const data = {
            amount: 1,
            product_id: productId,
            cart_id: cart.cart_id,
        };

        axios.post(`${apiUrl}cart_add_product/`, data, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(() => {
            console.log("Dodano produkt ", productId, "do koszyka: ", cart.cart_id);

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

    const getImageUrl = (productId) => `${apiUrl}get_product_image/${productId}`;

    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchText.toLowerCase())
    );

    const renderProduct = ({ item }) => (
        <TouchableOpacity style={styles.product} onPress={() => navigation.navigate('Product', { productId: item.id })}>
            <Image
                style={styles.productImage}
                source={{ uri: getImageUrl(item.id) }}
            />
            <Text style={styles.productName}>{item.name}</Text>
            <Text style={styles.productPrice}>Cena: {item.price} zł</Text>
            <TouchableOpacity style={styles.addButton} onPress={() => addToCart(item.id)}>
                <Text style={styles.buttonText}>Do koszyka</Text>
            </TouchableOpacity>
        </TouchableOpacity>
    );

    return (
        <>
            <FlatList
            data={filteredProducts}
            renderItem={renderProduct}
            keyExtractor={(item, index) => String(index)}
            numColumns={2}
            />
            <TextInput
                style={styles.searchField}
                inputMode='text'
                keyboardType='default'
                placeholder="&#128269; Szukaj..."
                value={searchText}
                onChangeText={text => setSearchText(text)}
            />
        </>
        
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
        width: '45%',
        alignItems: 'center',
    },
    productName: {
        fontSize: 25,
        fontWeight: 'bold',
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
    },
    searchField: {
        paddingLeft: 20,
        backgroundColor: '#d3eaf2',
        borderColor: '#e5e7eb',
        borderWidth: 2,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        opacity: 80,
        height: 40,
        paddingHorizontal: 10,
        alignSelf:'flex-end',
        width: '100%',
    }
});

export default HomeScreen;