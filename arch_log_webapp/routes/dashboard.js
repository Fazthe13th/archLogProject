const express = require('express');
router = express.Router()

const Logs = require('../models/Log');

router.get('/',async (req,res, next)=>
{
    var perPage = 10
    var page = req.query.page || 1
    let search_query = {};
    if (typeof req.query.source_ip != 'undefined' || typeof req.query.NAT_ip != 'undefined' || typeof req.query.destination_ip != 'undefined' || typeof req.query.month != 'undefined' || typeof req.query.day != 'undefined'){
        if (req.query.source_ip != '')
        {
            search_query['source_ip'] = req.query.source_ip;
        }
        if (req.query.NAT_ip != '')
        {
            search_query['NAT_ip'] = req.query.NAT_ip;
        }
        if (req.query.destination_ip != '')
        {
            search_query['destination_ip'] = req.query.destination_ip;
        }
        if (req.query.month != '')
        {
            search_query['month'] = req.query.month;
        }
        if (req.query.day != '')
        {
            search_query['day'] = req.query.day;
        }
    }
    else
    {
        search_quer = {}
    }
    await Logs
        .find(search_query)
        .skip((perPage * page) - perPage)
        .limit(perPage)
        .exec(function(err, logs) {
            Logs.countDocuments(search_query).exec(function(err, count) {
                if (err) return next(err)
                res.render('dashboard', {
                    logs: logs,
                    current: page,
                    pages: Math.ceil(count / perPage),
                    source_ip: search_query['source_ip'],
                    NAT_ip: search_query['NAT_ip'],
                    destination_ip: search_query['destination_ip'],
                    month: search_query['month'],
                    day:search_query['day']
                })
            })
        })
});

// router.post('/:page?', async (req,res, next) =>
// {
    
//     var perPage = 10
//     var page = req.params.page || 1
//     if (req.body.source_ip != '')
//     {
//         search_query['source_ip'] = req.body.source_ip;
//     }
//     if (req.body.NAT_ip != '')
//     {
//         search_query['NAT_ip'] = req.body.NAT_ip;
//     }
//     if (req.body.destination_ip != '')
//     {
//         search_query['destination_ip'] = req.body.destination_ip;
//     }
//     if (req.body.month != '')
//     {
//         search_query['month'] = req.body.month;
//     }
//     if (req.body.day != '')
//     {
//         search_query['day'] = req.body.day;
//     }
//     await Logs
//         .find({ source_ip: '45.113.132.18' })
//         .skip((perPage * page) - perPage)
//         .limit(perPage)
//         .exec(function(err, logs) {
//             Logs.countDocuments({ source_ip: '45.113.132.18' }).exec(function(err, count) {
//                 if (err) return next(err)
//                 res.render('dashboard', {
//                     logs: logs,
//                     current: page,
//                     pages: Math.ceil(count / perPage)
//                 })
//             })
//         })
 
// });

module.exports = router