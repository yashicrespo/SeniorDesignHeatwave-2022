var i = 0;
var url = "https://b2ue2x6yjh.execute-api.us-west-2.amazonaws.com/s3api/senddb1.txt"

fetch(url).then(function(response) {
    // The API call was successful!

   
  
  
    return response.json();
}).then(function(html) {
    // This is the HTML from our response as a text string
   
    console.log(html);
}).catch(function(err) {
    // There was an error
    console.warn('Something went wrong.', err);
});
console.log("Hello, world!");