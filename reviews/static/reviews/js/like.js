const likeBtnList = document.querySelectorAll('.likeBtn')
const URI = 'http://127.0.0.1:8000/reviews/'

const onClickAwait = async function (event) {
  const { reviewId } = event.target.dataset
  const likeCounter = document.querySelector(`#likeCounter${reviewId}`)
  
  try {
    const res = await axios(URI + reviewId + '/like/', {
      method: 'post',
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    })
    
    likeCounter.innerText = res.data.likeCounter
    event.target.innerText = res.data.isLike ? '좋아요 취소' : '좋아요'
  } catch (err) {
    console.error(err)
  }
}

likeBtnList.forEach(likeBtn => {
  likeBtn.addEventListener('click', onClickAwait)
})

