import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/home-screen';
import CartScreen from '../screens/cart-screen';
import ProductScreen from '../screens/product-screen';
import LoginScreen from '../screens/login-screen';
import RegisterScreen from '../screens/register-screen';
import OrderScreen from '../screens/order-screen';

const HomeStack = createStackNavigator();
const CartStack = createStackNavigator();
const AccountStack = createStackNavigator();
const Tab = createBottomTabNavigator();

function HomeStackScreen() {
    return (
        <HomeStack.Navigator
            screenOptions={{
                headerShown: false, // Ukrywa nagłówek dla wszystkich ekranów
            }}
        >
            <HomeStack.Screen name="Home" component={HomeScreen} />
            <HomeStack.Screen name="Product" component={ProductScreen} />
        </HomeStack.Navigator>
    );
}
  
function CartStackScreen() {
    return (
        <CartStack.Navigator
            screenOptions={{
                headerShown: false, // Ukrywa nagłówek dla wszystkich ekranów
            }}
        >
            <CartStack.Screen name="Cart" component={CartScreen} />
            <CartStack.Screen name="Order" component={OrderScreen} />
        </CartStack.Navigator>
    );
}

function AccountStackScreen() {
    return (
        <AccountStack.Navigator
            screenOptions={{
                headerShown: false, // Ukrywa nagłówek dla wszystkich ekranów
            }}
        >
            <AccountStack.Screen name="Login" component={LoginScreen} />
            <AccountStack.Screen name="Register" component={RegisterScreen} />
        </AccountStack.Navigator>
    );
}
  
export default function Navigator() {
    return (
        <Tab.Navigator
            screenOptions={{
                headerShown: false, // Ukrywa nagłówek dla wszystkich ekranów
            }}
        >
            <Tab.Screen name="HomeStack" component={HomeStackScreen} options={{ title: 'Sklep' }} />
            <Tab.Screen name="CartStack" component={CartStackScreen} options={{ title: 'Koszyk' }} />
            <Tab.Screen name="AccountStack" component={AccountStackScreen} options={{ title: 'Konto' }} />
        </Tab.Navigator>
    );
}
