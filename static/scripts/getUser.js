let data = []
const gettingdata = function () {
    const username = document.getElementById("username").value;
    if (username == ""){
        document.getElementById("username").focus();
    }
    console.log(username);

    axios({
        method:'GET',
        url: 'http://0.0.0.0:5000/api/v1/people/'.concat(username),
        }).then(res=> {
            data = res.data
            console.log(res)
        }).catch(error => console.log(error.response.data))

        console.log(data)
        const container = document.getElementById("main_container")
        container.appendChild("<img src="data.photo_url"> <h4>Name <h4> <p> data.name </p> <h4> Skills </h4> <p> </p>")

}