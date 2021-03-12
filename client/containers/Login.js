import React, { useState } from 'react'
import axios from 'axios'
import { useForm } from 'react-hook-form'

function Login({ history }) {
  const { register, handleSubmit, errors } = useForm()
  const [errorbox, updateErrorbox] = useState('')


  async function onSubmit(data) {

    updateErrorbox('')

    const formdata = {
      'email': data.email,
      'password': data.password
    }

    console.log(formdata)

    try {
      const { data } = await axios.post('/api/login', formdata,)
      if (localStorage) {
        localStorage.setItem('token', data.token)
      }      
      history.push('/search-home')
    } catch (err) {
      console.log(err.response.data)
    }
  }

  const backgroundStyle = {
    height: '100vh',
    background: 'url(https://i.pinimg.com/564x/df/05/80/df058037fef8b0773052fd0d9c6acb73.jpg)',
    backgroundSize: 'cover'
  }

  return (
    <div className='container'>
      <div className="hero is-fullheight-with-navbar is-primary">
        <div className="hero-body" style={backgroundStyle}>
          <h1 className="title has-text-centered">Login</h1>

          {errorbox && <div className='box has-background-danger has-text-white'>{errorbox}</div>}

          <form onSubmit={handleSubmit(onSubmit)} >

            <div className='field'>
              <label>
                <p>Email</p>
              </label>
              <input
                className={`input ${errors.email && 'is-danger'}`}
                name='email'
                placeholder='Email@email.com'
                type='text'
                defaultValue=''
                ref={register({ required: true })}
              />
              {errors.email && <div className='mt-2 mb-2 is-size-7'>This field is required</div>}
            </div>

            <div className='field'>
              <label>
                <p>Password</p>
              </label>
              <input
                className={`input ${errors.password && 'is-danger'}`}
                name='password'
                placeholder='Password'
                type='password'
                defaultValue=''
                ref={register({ required: true })}
              />
              {errors.password && <div className='mt-2 mb-2 is-size-7'>This field is required</div>}
            </div>

            <input
              className='button is-primary'
              type='submit'
            />

          </form >
        </div>
      </div>
    </div >
  )
}

export default Login