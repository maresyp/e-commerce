import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/home-screen';
import CartScreen from '../screens/cart-screen';
import ProductScreen from '../screens/product-screen';

const HomeStack = createStackNavigator();
const CartStack = createStackNavigator();
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
        </CartStack.Navigator>
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
        </Tab.Navigator>
    );
}
