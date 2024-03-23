import React, { useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, StyleSheet } from 'react-native';
import axios from 'axios';

const CartScreen = () => {
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

    return (
        <ScrollView>
            <Text>Tutaj będzie koszyk</Text>
        </ScrollView>
    );
};

export default CartScreen;