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

export default function Login({ navigation, route }) {
  const [username, setUsername] = useState(
    route.params ? route.params.username : ''
  );
  const [password, setPassword] = useState('')
  const [isIncorrect, setIncorret] = useState(false);
  const isConfirmed = route.params ? true : false

  const loginHandler = async () => {
    try {
      const user = await Auth.signIn(username, password);

      console.log(user);
      navigation.replace('Home');
    } catch (error) {
      console.log('error signing in', error);
      setIncorret(true);
    }
  };

  const resetHandler = () => {};

  const registerHandler = () => {
    navigation.navigate('Register');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.headerText}>Heatmap</Text>
      <View style={styles.form}>
        {isIncorrect ? (
          <Text style={styles.errorText}>
            Username or Password is incorrect
          </Text>
        ) :  isConfirmed ? (
          <Text style={styles.successText}>
            You have successfully registered!
          </Text>
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
          onChangeText={setPassword}
          value={password}
          placeholder="Password"
          secureTextEntry
        />
        <Pressable onPress={resetHandler}>
          <Text>Forgot Password?</Text>
        </Pressable>
      </View>
      <View style={styles.button}>
        <Button title="Sign in" color="#000000" onPress={loginHandler} />
      </View>
      <Pressable onPress={registerHandler}>
        <Text>Sign up here</Text>
      </Pressable>
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
  successText: {
    color: '#008800'
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
    marginBottom: 5,
  },
});
