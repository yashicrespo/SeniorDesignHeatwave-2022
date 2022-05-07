import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Amplify from 'aws-amplify'
import config from './src/aws-exports'

import Login from './src/screens/Login';
import Register from './src/screens/Register';
import Confirm from './src/screens/Confirm';
import Home from './src/components/Home';

export default function App() {
  const Stack = createNativeStackNavigator();
  
  Amplify.configure(config)

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ header: () => null }}
        />
        <Stack.Screen
          name="Register"
          component={Register}
          options={{ header: () => null }}
        />
        <Stack.Screen
          name="Confirm"
          component={Confirm}
          options={{ header: () => null }}
        />
        <Stack.Screen
          name="Home"
          component={Home}
          options={{ header: () => null }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
