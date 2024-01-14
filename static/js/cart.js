var updateBtns = document.getElementsByClassName('update-cart')

for ( var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId= this.dataset.product
        var action= this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:',user)
        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
    
        } else {
            // console.log('User is authenticated, sending data ...')
            updateUserOrder(productId, action)
        }

    })
}


function addCookieItem(productId, action){
	console.log('User is not authenticated !!!')

    if (action == 'add'){ //if we clicked on add product
		if (cart[productId] == undefined){ //if the product is not already in the cart, create it in the cart
		cart[productId] = {'quantity':1}

		}else{ //else if the product is already in the cart, just add one to its quantity
			cart[productId]['quantity'] += 1
		}
	}

    if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

    console.log('Cart:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/" // this resets/overides the cookie cart with updated values in case any change was made

    location.reload()
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data ...')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) => {
        location.reload()
    })
}
// // 
// // console.log('hello world')