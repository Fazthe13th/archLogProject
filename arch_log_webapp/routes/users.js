const express = require('express');
const router = express.Router();

//Load login page
router.get('/', (req,res) =>
{
    res.render('login');
});

//Login

router.post('/login',(req,res)=>
{
    const {username,password} = req.body;
    let  errors = [];
    //check for errors
    if(!username || !password)
    {
        errors.push({msg: "Please fill in all fields"});
    }
    if (errors.length > 0) {
        res.render('login', {errors});
    }
    else
    {
        res.send("Pass");
    }
});

module.exports = router