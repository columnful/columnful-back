// const followBtn = document.querySelector('#followBtn')
//   const followersCount = document.querySelector('#follwersCount')
//   followBtn.addEventListener('click', function (event) {
//     const userId = event.target.dataset.userId
//     const URI = `http://127.0.0.1:8000/accounts/${userId}/follow/`

//     const reqConfig = {
//       headers: {
//         'X-CSRFToken': Cookies.get('csrftoken')
//       }
//     }

//     axios.post(URI, {}, reqConfig)
//       .then(res => {
//         followersCount.innerText = res.data.followersCount
        
//         if (res.data.isFollow) {
//           event.target.innerText = 'Unfollow'
//           event.target.classList = 'btn btn-danger'
//         } else {
//           event.target.innerText = 'Follow'
//           event.target.classList = 'btn btn-primary'
//         }
//       })
//       .catch(err => console.error(err))
//   })

const followBtn = document.querySelector('#followBtn')
  const followersCount = document.querySelector('#followersCount')

  followBtn.addEventListener('click', function (event) {
    const userId = event.target.dataset.userId
    const URI = `http://127.0.0.1:8000/accounts/${userId}/follow/`
  
    const reqConfig = {
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
      }
    }

    axios.post(URI, {}, reqConfig)
      .then(res => {
        followersCount.innerText = res.data.followersCount
        
        if (res.data.isFollow){
          event.target.innerText = 'Unfollow'
          event.target.classList = 'btn btn-danger'
          
        } else {
          event.target.innerText = 'Follow'
          event.target.classList = 'btn btn-primary'
        }
      })
      .catch(err => console.error(err))
  })