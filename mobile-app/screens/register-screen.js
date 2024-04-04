import { View, Text, StyleSheet, TouchableOpacity, Platform } from 'react-native'
import { useNavigation } from '@react-navigation/native';
import { ScrollView, TextInput } from 'react-native-gesture-handler';

const RegisterScreen = () => {
    const navigation = useNavigation();
    const apiUrl = Platform.OS === 'ios' ? 'http://127.0.0.1:8000/api/' : 'http://10.0.2.2:8000/api/';

    return (
        <ScrollView style={styles.mainContainer}>
            <Text style={styles.mainText}>Zarejestruj konto</Text>

            <View style={styles.loginForm}>
                <Text style={styles.fieldName}>Imię:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='text'
                    keyboardType='default'
                    placeholder="Podaj swoje imię"
                />

                <Text style={styles.fieldName}>Adres e-mail:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='email'
                    keyboardType='email-address'
                    placeholder="Podaj adres e-mail"
                />

                <Text style={styles.fieldName}>Nazwa użytkownika:</Text>
                <TextInput
                    style={styles.inputField}
                    inputMode='text'
                    keyboardType='default'
                    placeholder="Podaj nazwę użytkownika"
                />

                <Text style={styles.fieldName}>Hasło:</Text>
                <TextInput
                    style={styles.inputField}
                    placeholder="Wprowadź hasło"
                    secureTextEntry
                />

                <Text style={styles.fieldName}>Potwierdzenie hasła:</Text>
                <TextInput
                    style={styles.inputField}
                    placeholder="Potwierdź hasło"
                    secureTextEntry
                />

                <TouchableOpacity style={styles.loginBtn} onPress={() => jakasFunkcja()}>
                    <Text style={styles.buttonText}>Zarejestruj się!</Text>
                </TouchableOpacity>

                <Text style={styles.subText2}>Masz już konto?</Text>
                <TouchableOpacity style={styles.signupBtn} onPress={() => navigation.navigate('Login')}>
                    <Text style={styles.signupText}>Zaloguj się!</Text>
                </TouchableOpacity>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    mainContainer: {
        marginHorizontal: '2.5%',
        marginVertical: '15%',
        paddingVertical: 20,
        borderRadius: 10,
        backgroundColor: '#f9f9f9',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.8,
        shadowRadius: 2,
        elevation: 5,
        width: '95',
    },
    mainText: {
        fontSize: 30,
        fontWeight: 'bold',
        alignSelf: 'center',
    },
    subText: {
        color: '#949494',
        fontSize: 15,
        alignSelf: 'center',
    },
    subText2: {
        color: '#949494',
        fontSize: 15,
        alignSelf: 'flex-end',
    },
    loginForm: {
        width: '80%',
        alignSelf:  'center',
        marginVertical: 20,
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
    loginBtn: {
        backgroundColor: '#299ad7',
        marginVertical: 20,
        borderRadius: 10,
        padding: 5,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.9,
        shadowRadius: 2,
        elevation: 5,
        width: '80%',
        alignSelf:  'center',
    },
    buttonText: {
        color: 'white',
        fontSize: 20,
        textAlign: 'center',
    },
    signupBtn: {
        alignSelf: 'flex-end',
    },
    signupText: {
        color: '#0051ff',
        fontSize: 15,
    }
});

export default RegisterScreen;