
import React, { useEffect, useState } from 'react';
import { Button, Dimensions, Image, StyleSheet, View, Text } from 'react-native';

export default function Dashboard({ navigation, route }) {
  const id = route.params.id;
  const [uri, setUri] = useState(
    'https://inrr1rfk38.execute-api.us-east-2.amazonaws.com/v2/imagetest23?file=plot.jpg'
  )
  const [count, setCount] = useState(0)

  useEffect(() => {
    setInterval(() => { 
      setUri('https://inrr1rfk38.execute-api.us-east-2.amazonaws.com/v2/imagetest23?file=plot.jpg') 
      setCount(prevState => prevState + 1)
    }, 5000)
  }, [])

  return (
    <View style={styles.container}>
      <Image
        style={styles.heatmap}
        source={{
          uri: uri,
        }}
      />
      <Text>Update counter: {count}</Text>
      <View style={styles.backButton}>
        <Button title="Back" color="#000000" onPress={navigation.goBack} />
      </View>
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
  bodyText: {
    margin: 20,
    fontSize: 15,
    fontWeight: '300',
  },
  heatmap: {
    width: Dimensions.get('window').width,
    height: undefined,
    aspectRatio: 360 / 240
  },
  backButton: {
    marginVertical: 40,
  },
});
