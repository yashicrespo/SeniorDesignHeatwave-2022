import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import CameraOptions from '../screens/CameraOptions';
import CameraView from '../screens/CameraView';

export default function Cameras() {
  const Stack = createNativeStackNavigator();

  return (
    <Stack.Navigator initialRouteName="CameraOptions">
      <Stack.Screen
        name="CameraOptions"
        component={CameraOptions}
        options={{ header: () => null }}
      />
      <Stack.Screen
        name="CameraView"
        component={CameraView}
        options={{ header: () => null }}
      />
    </Stack.Navigator>
  );
}
