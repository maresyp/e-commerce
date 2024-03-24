import { StyleSheet, Text, View, Image } from 'react-native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Navigator from './components/navigator';
import { NavigationContainer } from '@react-navigation/native';
import { SafeAreaView } from 'react-native-safe-area-context';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <SafeAreaView style={{ flex: 1 }}>
        <Image
          source={{ uri: 'http://10.0.2.2:8000/static/images/logo.png' }}
          style={styles.logo}
        />
        <View style={styles.header}>
        </View>
        <Navigator/>
      </SafeAreaView>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  header: {
    height:'7%',
    overflow: 'visible',
  },
  logo: {
    position: 'absolute', // Pozycjonowanie absolutne
    top: 30, // Odległość od górnej krawędzi
    left: '10%', // Odległość od lewej krawędzi
    width: 120, // Szerokość logo
    height: 70, // Wysokość logo
    zIndex: 1,
  }
});
