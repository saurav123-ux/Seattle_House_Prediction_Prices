function getBathroomsValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
  }
  
  function getBedroomsValue() {
    var uiBedrooms = document.getElementsByName("uiBedrooms");
    for(var i in uiBedrooms) {
      if(uiBedrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft_living= document.getElementById("uiSqft");
    var bedrooms = getBedroomsValue();
    var bathrooms = getBathroomsValue();
    var grade = document.getElementById("uigrade");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price";
    
  
    $.post(url, {
        sqft_living: parseFloat(sqft_living.value),
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        grade: grade.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_grade_names"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_grade_names request");
        if(data) {
            var grade = data.grade;
            var uigrade = document.getElementById("uigrade");
            $('#uigrade').empty();
            for(var i in grade) {
                var opt = new Option(grade[i]);
                $('#uigrade').append(opt);
            }
        }
    });
  }
  
  window.onload=onPageLoad;
