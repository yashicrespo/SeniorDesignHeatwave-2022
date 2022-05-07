import React, { useState } from 'react';
import {
  Button,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { Auth } from 'aws-amplify';

export default function Register({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [isIncorrect, setIncorret] = useState(false);

  const registerHandler = async () => {
    try {
      const { user } = await Auth.signUp({
        username,
        password,
        attributes: {
          email,
        },
      });

      console.log(user);
      navigation.navigate('Confirm', { username });
    } catch (error) {
      console.log('error signing up:', error);
      setIncorret(true);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.headerText}>Heatmap</Text>
      <View style={styles.form}>
        {isIncorrect ? (
          <Text style={styles.errorText}>Incorrect information provided</Text>
        ) : (
          <></>
        )}
        <TextInput
          style={styles.input}
          onChangeText={setUsername}
          value={username}
          placeholder="Username"
        />
        <TextInput
          style={styles.input}
          onChangeText={setEmail}
          value={email}
          placeholder="Email"
        />
        <TextInput
          style={styles.input}
          onChangeText={setPassword}
          value={password}
          placeholder="Password"
          secureTextEntry
        />
        <Pressable onPress={() => navigation.navigate('Confirm')}>
          <Text>Have a confirmation code?</Text>
        </Pressable>
      </View>
      <View style={styles.button}>
        <Button title="Sign up" color="#000000" onPress={registerHandler} />
      </View>
      <View style={styles.button}>
        <Button
          title="Back"
          color="#000000"
          onPress={() => {
            navigation.navigate('Login');
          }}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerText: {
    marginBottom: 20,
    fontSize: 25,
    fontWeight: '700',
    textTransform: 'uppercase',
  },
  errorText: {
    color: '#ff0000',
  },
  form: {
    marginBottom: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    height: 40,
    width: 250,
    margin: 5,
    borderWidth: 1,
    padding: 10,
  },
  button: {
    width: 80,
    marginBottom: 5
  },
});
