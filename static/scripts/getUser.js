const gettingdata = function () {
    const username = document.getElementById("username").value;
    if (username == ""){
        document.getElementById("username").focus();
    }
    console.log(username);

    axios({
        method:'GET',
        url: 'http://127.0.0.1:5000/people/'.concat(username)
        }).then(res=> {
            console.log(res)
        })
}