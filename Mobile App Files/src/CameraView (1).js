import React, { useEffect, useState } from 'react';
import { Button, Dimensions, Image, StyleSheet, View, Text } from 'react-native';

export default function Dashboard({ navigation, route }) {
  const id = route.params.id;
  const [temps, setTemps] = useState()
  const [uri, setUri] = useState(
    'https://44y88f70a3.execute-api.us-east-2.amazonaws.com/v1/imagetest22?file=plot.jpg'
  )

  useEffect(async () => {
    let interval = setInterval(() => { 
      setUri('https://44y88f70a3.execute-api.us-east-2.amazonaws.com/v1/imagetest22?file=plot.jpg') 
      
      const res = await fetch(`https://m6b1v8pzje.execute-api.us-west-2.amazonaws.com/hwcam/camid/1`);
      setTemps(res)
    }, 5000)

    return () => {
      clearInterval(interval);
    };
  }, [])

  return (
    <View style={styles.container}>
      <Image
        style={styles.heatmap}
        source={{
          uri: uri,
        }}
      />
      {temps ? <Text>Person: {temps.PersonTemp} Room: {temps.RoomTemp}</Text> : <></>}
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
