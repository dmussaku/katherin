var webpack = require('webpack');
var path = require('path')

module.exports = {
    entry: {
        build: './src/main.js'
    },
    module: {
        loaders: [
            {
                test: /\.vue$/,
                loader: 'vue'
            },
            {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'url-loader'
            }
        ],
        resolve: {
            extensions: ['', '.js', '.vue'],
            fallback: [path.join(__dirname, '../node_modules'), path.join(__dirname, './dist')],
            alias: {vue: 'vue/dist/vue'}
        }
    },
}

if (process.env.NODE_ENV === 'production') {
    module.exports.output = {
        path: path.join(__dirname, './dist/static'),
        publicPath : '/dist/static',
        filename: 'build.js'
    }
    module.exports.plugins = [
        new webpack.optimize.UglifyJsPlugin(
            {
                minimize: true,
                compress: {
                    warnings: false
                }
            }
        )
    ]
} else {
    module.exports.output = {
        path: path.join(__dirname, './dist'),
        publicPath : '/dist/',
        filename: '[name].js'
    }
}