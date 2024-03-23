import React, { useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, StyleSheet, FlatList, Button, TouchableOpacity } from 'react-native';
import axios from 'axios';

const HomeScreen = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://10.0.2.2:8000/api/get_all_products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const getImageUrl = (productId) => `http://10.0.2.2:8000/api/get_product_image/${productId}`;

    const renderProduct = ({ item }) => (
        <View style={styles.product}>
            <Image
                style={styles.productImage}
                source={{ uri: getImageUrl(item.id) }}
            />
            <Text style={styles.productName}>{item.name}</Text>
            <Text style={styles.productPrice}>Cena: {item.price} zł</Text>
            <TouchableOpacity style={styles.addButton}>
                <Text style={styles.buttonText}>Do koszyka</Text>
            </TouchableOpacity>
        </View>
    );

    return (
        <FlatList
            data={products}
            renderItem={renderProduct}
            keyExtractor={(item, index) => String(index)}
            numColumns={2}
        />
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
    },
    buttonText: {
        color: 'white',
        fontSize: 20,
    }
});

export default HomeScreen;