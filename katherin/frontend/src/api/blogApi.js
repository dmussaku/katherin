import axios from 'axios'
import { HOST } from '../settings.js'
var APIurl = HOST + '/api/v1/blog/'

const API = {
	getArticles: function(callback){
		axios.get(APIurl + 'articles/?format=json')
			.then(function(response) {
				callback(response, true)
			})
			.catch(function(response) {
				console.log(error)
				callback(error, false)
			})
	},
	getPosts: function(callback){
		axios.get(APIurl + 'posts/?format=json')
			.then(function(response) {
				callback(response, true)
			})
			.catch(function(response) {
				console.log(error)
				callback(error, false)
			})
	}
}

export {
	API,
}