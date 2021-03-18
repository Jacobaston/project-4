const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
// const WorkboxPlugin = require('workbox-webpack-plugin')
// const CopyWebpackPlugin = require('copy-webpack-plugin')
const Dotenv = require('dotenv-webpack')
const env = process.env.NODE_ENV === 'production' ? (
  new webpack.EnvironmentPlugin({ ...process.env })
) : (
  new Dotenv()
)

module.exports = () => {
  return {
    entry: './client/index.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve('server/dist'),
      publicPath: '/'
    },
    devtool: 'source-map',
    module: {
      rules: [
        { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ },
        { test: /\.css$/, use: ['style-loader', 'css-loader'] },
        { test: /\.s(a|c)ss$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
        { test: /\.(png|jpe?g|gif|svg)$/i, use: 'file-loader' }
      ]
    },
    devServer: {
      contentBase: path.resolve('client'),
      hot: true,
      open: true,
      port: 8001,
      watchContentBase: true,
      historyApiFallback: true,
      proxy: {
        '/api': {
          target: 'http://localhost:5000',
          secure: false
        }
      }
    },
    plugins: [
      new Dotenv(),
      new webpack.HotModuleReplacementPlugin(),
      new HtmlWebpackPlugin({
        // title: 'Garms',
        template: 'client/index.html',
        filename: 'index.html',
        inject: 'body'
      }),
      // new WorkboxPlugin.GenerateSW({
      //   clientsClaim: true,
      //   skipWaiting: true
      // }),
      // new CopyWebpackPlugin([
      //   { from: '/manifest', to: 'manifest' }
      // ]),
      // new webpack.HotModuleReplacementPlugin(),
      env
    ]
  }
}
