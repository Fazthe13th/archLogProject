const express = require('express');
const expressLayouts = require('express-ejs-layouts');
require('dotenv/config')
const mongoose = require('mongoose');
const app = express();

// EJS
app.use(expressLayouts);
// app.set('views', '/views');
app.set('view engine', 'ejs');

//Connect to database
mongoose.connect(process.env.DB_URL, { useNewUrlParser: true, useUnifiedTopology: true })
.then(()=> console.log('MongoDB Connected..'))
.catch(err => console.log(err));
//Make public static
app.use('/public', express.static('public'));

//Body parser
app.use(express.urlencoded({extended: false}));
//Routes
// app.use('/', require('./routes/index'));
app.use('/', require('./routes/users'));
app.use('/dashboard/', require('./routes/dashboard'));

const PORT = process.env.PORT || 5000;

app.listen(PORT,console.log(`Server started on ${PORT}`));