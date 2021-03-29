### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly, Software Engineering Immersive
# Garms

## Overview

![Logo](readme_assets/logo.png)

Check it out [here](https://ja-garms.herokuapp.com/)

## The Brief

* **Build a full-stack application** by making your own back-end and your own front-end
* **Use an Flask API** to serve your data from a Postgres database
* **Consume your API with a separate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models
* **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut
* **Be deployed online** so it's publicly accessible.

## Technologies Used

### Back-end:
- Python
- Flask
- Flask SQLAlchemy
- Blueprint
- Marshmallow
- JWT
- PyTest

### Frontend:
- React.js
- Axios
- Webpack
- React-router-dom
- React-Hooks
- Bulma
- Nodemailer

### Development tools:
- VS code
- Pipenv/npm
- Insomnia
- Git
- Github
- Google Chrome dev tools
- Heroku (deployment)
- Trello Board (planning and timeline)
- PhotoShop (wireframing)
- Zoom
- Slack

## Approach taken

### Day 1 - Planning

As a group we decided very quickly on the idea of Garms for this project and that we all wanted to be involved in the full-stack development of the app. We also decided early on that we should develop it to be fully responsive initially built mobile first. With that in mind we used photoshop to create a storyboard/wireframe as well QuickDBD for the models we required and the relationships between them.

![Database relationships](readme_assets/relationship.png)
  
![Wireframe](readme_assets/wireframe.png)
  
We decided early on to keep a high level of communication throughout the project. We started each day with a 30-minute stand up discussion where we would talk about our current tasks and if we had any blockers. We were then on a Zoom meeting and Slack throughout the day so we could keep in contact should we need any quick bug fixing etc. We used Git and GitHub for version control and decided for the first few days to do our pushes and pulls together to aviod any potential Git issues or merge conflicts that may arise. We delegated the work evenly between us and used Trello to create a to-do list that we would all keep on top of throughout the project.

![Trello](readme_assets/mvp.png)

### Back-end - Day 2 & 3

This was my first experience of creating a back-end using Python. We used Flask REST Framework to create a PostgreSQL database with RESTful features. As Python and Flask were new technologies to us, we all wanted to increase our experience. Therefore, we pair (triple) programmed the backend.

As a result of our substantial planning, we were confident in the relationships between each of our models. There were four models in total (product, user, wishlist and order history), as well as the base model.

Below is the product model, and it was important here to ensure the ForiegnKey and relationships between models were correct. One area I found challenging intially was the cascading e.g. if a user account was deleted, this should not delete the product as this would still need to show in a buyer's account. Once I understood this, finalising the models was much easier.

```py
class Product(db.Model, BaseModel):
    __tablename__ = "product"

    product_name = db.Column(db.Text, nullable=False)
    product_image = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=True)
    size = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    condition = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))

    wishlist = db.relationship('Wishlist', backref='product', cascade="all, delete")
    order_history = db.relationship('OrderHistory', backref='product', cascade="all, delete")
```

Once we had the models set up, we split the controllers that would be required and all wrote a proportion each. I took ownership of the product and user controllers.

Serializers were also created and these were tested in Table Plus to ensure we had all the required data. Due to the relationships between tables, all schemas had nested fields. To ensure that there were no circular import errors, 'simple' schemas were created. An example of this is below; in the user schema, the product, order history and wishlist IDs were nested. We wanted to be able to see the ID of the user which a product related to, so SimpleUserSchema was created so that this could be nested within the ProductSchema.

```py
from app import ma
from models.user import User
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',)
        load_only = ('password')

    password = fields.String(required=True)
    product = fields.Nested('ProductSchema', many=True)
    order_history = fields.Nested('OrderHistorySchema', many=True)
    wishlist = fields.Nested('WishlistSchema', many=True)

    class SimpleUserSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = User
            load_instance = True
            exclude = ('password_hash', 'first_name', 'last_name', 'location', 'created_at')
            load_only = ('email', 'password')

        password = fields.String(required=True)
```

Pytest was used for the testing on the backend, and each endpoint had a test associated to it; by the end of the project, all 16 tests passed. Testing was very important to us as we wanted to limit the amount of debugging time when writing the controllers for our backend. By having clear tests for each controller we could make sure that each endpoint would behave excatly as we expected before writing any code.

```py
from app import app, db
import json
from tests.lib import login

def test_get_user():

    client = app.test_client()
    response = client.get("/api/users")

    assert len(response.json) == 4
    assert response.status_code == 200

def test_single_user():

    client = app.test_client()
    response = client.get("/api/users/1")

    assert response.json['username'] == 'indiak'
    assert response.status_code == 200 

def test_signup():

    client = app.test_client()

    user_data = {"username": "sam", "email": "sam@sam.com", "password": "sam123", "first_name": "Sam", "last_name": "Jones", "image": "TODO", "location": "London"}
    user_response = client.post(
        "/api/signup",
        data=json.dumps(user_data),
        content_type="application/json"
    )

    assert user_response.json['username'] == 'sam'
    assert user_response.status_code == 201

def test_login():

    client = app.test_client()

    login_data = {"password": "jake123", "email": "jake@jake.com"}
    response = client.post(
        "/api/login",
        data=json.dumps(login_data),
        content_type="application/json"
    )

    assert response.json["message"] == "Welcome back!"
    assert response.status_code == 200

def test_delete_user():

    client = app.test_client()

    login_data = {"password": "ben123", "email": "ben@ben.com"}
    login_response = client.post(
        "/api/login", data=json.dumps(login_data), content_type="application/json"
    )
    token = login_response.json["token"]

    user_data = {"username": "ben", "email": "ben@ben.com", "password": "ben123", "first_name": "Ben", "last_name": "Simpson", "image": "TODO", "location": "London"}
    request_headers = {"Authorization": f"Bearer {token}"}

    user_response = client.delete(
        "/api/users/4",
        data=json.dumps(user_data),
        content_type="application/json",
        headers=request_headers,
    )

    assert user_response.json['message'] == 'User deleted successfully'
    assert user_response.status_code == 200

def test_update_user():

    client = app.test_client()  

    token = login(client)

    update_request = {"location": "Sydney"}
    request_headers = {"Authorization": f"Bearer {token}"}
    user_response = client.put(
        "/api/users/2",
        data=json.dumps(update_request),
        content_type="application/json",
        headers=request_headers,
    )

    assert user_response.json["location"] == "Sydney"
    assert user_response.status_code == 200
```

### Front-end - Day 4, 5, 6, 7

Once the back end was complete, we split the front end tickets which had been created in Trello. I will discuss the pages which I took ownership of, and I also supported India and Hannah with de-bugging the other pages. For styling, we decided to use Bulma due to it being a mobile first framework.

#### Registration & login 

Registration had to allow a user to creat a profile by filling out a form and submitting the data to our database, for this we used 'React-forms'. By using React-forms we could benefit from built in validation on each input field, this would make sure that the user would input data in the way in which we would like it to be stored.

```py
  async function onSubmit(data) {
    updateErrorbox('')
    const formdata = {
      'username': data.username,
      'email': data.email,
      'password': data.password,
      'first_name': data.first_name,
      'last_name': data.last_name,
      'location': data.location,
      'image': 'https://i.ibb.co/6Zyw6CD/garms-icon.png'
    }

    try {
      const { data } = await axios.post('/api/signup', formdata,)
      if (data.id) {
        history.push('/login/success')
      } else {
        updateErrorbox('Unable to register user. Username and email address must be unique.')
      }
    } catch (err) {
      console.log(err.response.data)
    }
  }
```
<br/>

```py
{errorbox && <div className='box has-background-danger has-text-white'>{errorbox}</div>}

            <form onSubmit={handleSubmit(onSubmit)} >

              <div className='field'>
                <label>
                  <p>Username</p>
                </label>
                <input
                  className={`input ${errors.username && 'is-danger'}`}
                  name='username'
                  placeholder='Username'
                  type='text'
                  defaultValue=''
                  ref={register({ required: true })}
                />
                {errors.username && <div className='mt-2 mb-2 is-size-7'>This field is required</div>}
              </div>
```
Once the user has created the profile they are then redirected to the login page, in which they would have to enter their uniquie email and password in order to access their newly created profile.

#### Single Page

The single product page shows an image of the product, and information about this, including a description, brand, price, size and condition. You can also see the seller's details and a link to their profile page, so you can view other items that they are currently selling.

This page shows different buttons, dependent on whether you were the owner of the listing or not. If you were the owner of the listing, you are able to click buttons to edit or delete the listing.

```js
{product.user && <>
  {loggedInUserId === product.user.id &&
  <>
    {product.in_stock &&
      <>
        <Link to={`/productform/${productId}`} className="button is-primary">Edit</Link>
        <button className="button is-primary" onClick={handleDelete}>Delete</button>
      </>
     }
   </>
  }
</>}
```

If you are not the owner, you can add or remove the listing from your wishlist, dependent on the current state (true/false) of inWishList.

```js
{loggedInUserId !== product.user.id && <>
  {inWishlist ?
    <button className="button" onClick={removeFromWishlist}><i className='fas fa-heart mr-2'></i> Remove From Wishlist</button>
    :
    <button className="button" onClick={handleWishlist}><i className='fas fa-heart mr-2'></i> Add To Wishlist</button>
}
```

The below function would renders a buy now button if the current user is not the owner and if the product is in stock. The button is a link, which takes the user to 'checkout' to buy the item.

```js
function handleInStock() {
    if (loggedInUserId === (product.user && product.user.id)) {
      return
    } else {
      if (product.in_stock === true) {
        return <>
          <Link className="button is-primary" to={{%
            pathname: '/checkout',
            state: {%
              product: product
            %}
          %}}>Buy now</Link>
        </>
      }
    }
  }
```

#### Facebook Share

In order to make our Garms app more of a social experience we wanted users to be able to share any of the items via social media, this was done through a react compnent called 'React-share'. We implimented this on the single item page, where once the user clicks on the share button they will be redirected to a new window. The user can then compose a Facebook post and share the exact URL of any particualr item on the Garms app.

```js
import React from 'react'
import { FacebookShareButton } from 'react-share'

export default function ShareButtonFacebook({ productId }) {
  const shareButtonProps = {
    url: `https://ja-garms.herokuapp.com/products/${productId}`,
    network: 'Facebook',
    text: 'Check out this cool listing on Garms!',
    longtext:
      ''
  }

  return <FacebookShareButton {...shareButtonProps}>
    <div className="button facebook" ><i className='fab fa-facebook-f mr-2'></i>Share</div>
  </FacebookShareButton>

}
```

### Deployment

The app was then deployed through Heroku. Initially we linked up the front-end to the back-end and tested locally, and once we were happy with this then hit the deploy button on Heroku through the CLI. Once the app was then deployed online we seeded in the relevent data.

## Challenges
- Python and Flask were new technologies for this project, so it took slightly longer than expected to determine the relationships between the tables. However, it was a great learning experience.

## Wins
- The project was a great opportunity to learn Python, Flask and using a PostgreSQL database, as this was my first opportunity to do so.
- I am becoming more comfortable with React and trying out new libraries.

## Key Learnings


## Future Improvements
- Include password confirmation on the registration page
- Allow a user to sell more than one of each item, and subsequently show how many of a particular item are available on the single item page.
- Front end testing
- Allow in app messging between users so that they can negotiate or confirm things about any particular items

## Results

![Logo](readme_assets/logo.png)
