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
        url: 'https://torre-teams.herokuapp.com/api/v1/people/'.concat(username),
        }).then(res=> {
            user = JSON.parse(res.data)
            console.log(user)
            console.log(typeof(user))

        }).catch(error => console.log(error.response.data))
        console.log(type(user))
}