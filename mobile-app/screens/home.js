import React, { useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, StyleSheet } from 'react-native';
import axios from 'axios';

const HomeScreen = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/get_all_products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const getImageUrl = (productId) => `http://127.0.0.1:8000/api/get_product_image/${productId}`;

    return (
        <ScrollView>
            {products.map((product, index) => (
                <View key={index} style={styles.product}>
                    <Text style={styles.productName}>{product.name}</Text>
                    <Image
                        style={styles.productImage}
                        source={{ uri: getImageUrl(product.id) }}
                    />
                    <Text style={styles.productDescription}>Opis: {product.description}</Text>
                    <Text style={styles.productPrice}>Cena: {product.price} zł</Text>
                </View>
            ))}
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    product: {
        marginBottom: 20,
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
    },
    productName: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    productImage: {
        width: 200,
        height: 200,
        marginVertical: 10,
    },
    productDescription: {
        fontSize: 16,
    },
    productPrice: {
        fontSize: 16,
        fontWeight: 'bold',
    },
});

export default HomeScreen;