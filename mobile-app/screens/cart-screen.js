import React, { useCallback, useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, StyleSheet } from 'react-native';
import axios from 'axios';
import { useFocusEffect } from '@react-navigation/native';
import { useCart } from '../context/CartContext';

const CartScreen = () => {
    const { cart } = useCart();

    return (
        <ScrollView>
            <Text>{cart.cart_id}</Text>
            <Text>{cart.amount_of_products}</Text>
            <Text>{cart.total_price}</Text>
        </ScrollView>
    );
};

export default CartScreen;