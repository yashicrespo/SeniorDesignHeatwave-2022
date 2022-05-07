var i = 0;
var url = "https://b2ue2x6yjh.execute-api.us-west-2.amazonaws.com/s3api/wave.txt"
    //disp most recent alert
fetch(url).then(function(response) {
    // The API call was successful!
    return response.json();
}).then(function(html) {
    // This is the HTML from our response as a text string
    console.log(html.length);
    console.log(html);
    console.log(html[10].Time);
    var count = 0;

    for (var i = html.length - 1; i >= html.length - 6; i--) {
        count++;
        if (i < 0) { break; }
        var cam = 'cam' + count;
        document.getElementById(cam).innerHTML =
            "CamId : " + html[i].CamId + ", " +
            "Date : " + html[i].Date + ", " +
            "Time : " + html[i].Time + ", " +
            "PersonTemp : " + html[i].PersonTemp;

    }

}).catch(function(err) {
    // There was an error
    console.warn();
});

//More alert based on search date
function add() {
    var datess = document.getElementById("fNum");
    var dates = "";
    var cat = 90;
    if (datess) {
        dates = datess.value;
        const dval = dates[5] + dates[6] + '/' + dates[8] + dates[9] + '/' + dates[2] + dates[3];
        document.getElementById("txt").innerHTML = dval;


        //--------------------more alert by calander fetch

        fetch("https://b2ue2x6yjh.execute-api.us-west-2.amazonaws.com/s3api/wave.txt").then(function(response) {
            // The API call was successful!
            return response.json();
        }).then(function(html) {
            // This is the HTML from our response as a text string
            // console.log(html.length);
            //console.log(html);
            //  console.log(html[30].Time);
            var lengA = html.length; //-----------------------------------------------length of array to loop and find the matching char

            var catt = html[0].Date + "vats";
            console.log(dval);


            let morealert = []; //-------------------------------------------------------//array to store searched value of date

            var cc = 0;
            //=========================================clear cacalId
            /*
            for (var i = 0; i <= html.length - 1; i++) {


                count++;
                var cam = 'camcal' + count;
                document.getElementById(cam).innerHTML = "";
                //document.getElementById('camm').innerHTML = catt;

            }
*/
            /////////////////////////////////////////////////////
            var count = 0;
            var i = 0;
            for (i; i <= html.length - 1; i++) {
                //==========================for loop
                if (dval == html[i].Date) {
                    count++;
                    var cam = 'camcal' + count;
                    document.getElementById(cam).innerHTML =
                        "CamId : " + html[i].CamId + ", " +
                        "Date : " + html[i].Date + ", " +
                        "Time : " + html[i].Time + ", " +
                        "PersonTemp : " + html[i].PersonTemp;
                    //document.getElementById('camm').innerHTML = catt;
                } //==================================for loop
            }
            var carr = count + 1;
            for (carr; carr <= html.length; carr++) {
                var cam = 'camcal' + carr;
                document.getElementById(cam).innerHTML = "";
            }


            console.log(carr);
        }).catch(function(err) {
            // There was an error
            console.warn();
        });






        //--------------------------------------------cal fetch
    }





}