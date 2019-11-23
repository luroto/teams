const gettingdata = function () {
    let user = []
    let html = []
    const username = document.getElementById("username").value;
    if (username == ""){
        document.getElementById("username").focus();
    }
    console.log(username);

    axios({
        method:'GET',
        url: 'http://0.0.0.0:5000/api/v1/people/'.concat(username),
        }).then(res=> {
            user = JSON.parse(res.data)
            console.log(user)
        }).catch(error => console.log(error.response.data))
    }