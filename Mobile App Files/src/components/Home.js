import React from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Auth } from 'aws-amplify';
import Ionicons from '@expo/vector-icons/Ionicons';

import Dashboard from '../screens/Dashboard';
import Cameras from '../components/Cameras';
import Settings from '../screens/Settings';

export default function Home({ navigation }) {
  const Tab = createBottomTabNavigator();

  const logoutHandler = async () => {
    try {
      await Auth.signOut();
      navigation.replace('Login');
    } catch (error) {
      console.log('error signing out: ', error);
    }
  };

  return (
    <Tab.Navigator
      initialRouteName="Dashboard"
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          switch (route.name) {
            case 'Dashboard':
              iconName = focused ? 'clipboard' : 'clipboard-outline';
              break;
            case 'Cameras':
              iconName = focused ? 'videocam' : 'videocam-outline';
              break;
            case 'Settings':
              iconName = focused ? 'settings' : 'settings-outline';
              break;
            default:
              iconName = focused ? 'clipboard' : 'clipboard-outline';
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#000000',
        tabBarInactiveTintColor: '#444444',
        headerStyle: { backgroundColor: '#000000' },
        headerRight: () => (
          <View style={styles.button}>
            <Button title="Sign out" color="#000000" onPress={logoutHandler} />
          </View>
        ),
        tabBarShowLabel: false,
      })}
    >
      <Tab.Screen
        name="Dashboard"
        component={Dashboard}
        options={{
          headerTitle: () => <Text style={styles.headerText}>Dashboard</Text>,
        }}
      />
      <Tab.Screen
        name="Cameras"
        component={Cameras}
        options={{
          headerTitle: () => <Text style={styles.headerText}>Cameras</Text>,
        }}
      />
      <Tab.Screen
        name="Settings"
        component={Settings}
        options={{
          headerTitle: () => <Text style={styles.headerText}>Settings</Text>,
        }}
      />
    </Tab.Navigator>
  );
}

const styles = StyleSheet.create({
  headerText: {
    color: '#ffffff',
    fontSize: 25,
    fontWeight: '600',
    textTransform: 'capitalize',
  },
  button: {
    marginHorizontal: 20,
  },
});
