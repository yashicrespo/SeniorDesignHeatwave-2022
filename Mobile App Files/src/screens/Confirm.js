import React, { useState } from 'react';
import {
  Button,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { Auth } from 'aws-amplify';

export default function Confirm({ navigation, route }) {
  const [username, setUsername] = useState(
    route.params ? route.params.username : ''
  );
  const [code, setCode] = useState('');
  const [isIncorrect, setIncorret] = useState(false);
  const isCodeSent = route.params ? true : false;

  const confirmHandler = async () => {
    try {
      await Auth.confirmSignUp(username, code);
      navigation.replace('Login', { username });
    } catch (error) {
      console.log('error confirming sign up', error);
      setIncorret(true);
    }
  };

  const backHandler = () => {
    navigation.navigate('Login');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.headerText}>Heatmap</Text>
      <View style={styles.form}>
        {isIncorrect ? (
          <Text style={styles.errorText}>Username or Code is incorrect</Text>
        ) : isCodeSent ? (
          <Text style={styles.successText}>
            A confirmation code has been sent to your email
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
          onChangeText={setCode}
          value={code}
          placeholder="Code"
        />
      </View>
      <View style={styles.button}>
        <Button title="Confirm" color="#000000" onPress={confirmHandler} />
      </View>
      <View style={styles.button}>
        <Button title="Back" color="#000000" onPress={backHandler} />
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
  successText: {
    color: '#008800',
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
