import React, { useState, useEffect } from 'react';
import {
  Button,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';

export default function Dashboard({ navigation }) {
  const pressHandler = (id) => {
    navigation.navigate('CameraView', {id});
  };

  return (
    <View style={styles.container}>
      <Pressable style={styles.box} onPress={() => pressHandler(1)}>
        <Text>Camera 1</Text>
      </Pressable>
      <View style={styles.separator} />
      <Pressable style={styles.box} onPress={() => pressHandler(2)}>
        <Text>Camera 2</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box: {
    flex: 1,
    flexDirection: 'column',
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
  },
  separator: {
    width: '100%',
    height: 1,
    backgroundColor: '#000000',
  },
});
