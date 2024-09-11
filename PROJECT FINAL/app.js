const express = require('express');
const path = require('path');   
const app = express();
const port = process.env.PORT || 80;


// Express specific configurations
app.use('/static', express.static(path.join(__dirname,'static')));

// PUG specific configurations
app.set('view engine', 'pug');
app.set('views', path.join(__dirname,'views'));

app.get('/', (req, res)=>{
    res.status(200).render('home');
});
app.get('/Gallery', (req, res)=>{
    res.status(200).render('gallery');
});
// ALL COURSES --------------------------------

app.get('/Course', (req, res)=>{
    res.status(200).render('Course');
});
app.get('/ComputerScienceTechnology', (req, res)=>{
    res.status(200).render('ComputerScienceTechnology');
});
app.get('/Electronics', (req, res)=>{
    res.status(200).render('Electronics');
});
app.get('/Electrical', (req, res)=>{
    res.status(200).render('Electrical');
});
app.get('/Mechanical', (req, res)=>{
    res.status(200).render('Mechanical');
});
app.get('/Civil', (req, res)=>{
    res.status(200).render('Civil');
});
app.get('/Admission', (req, res)=>{
    res.status(200).render('Admission');
});
app.get('/About_us', (req, res)=>{
    res.status(200).render('About_us');
});
app.get('/Contact_us', (req, res)=>{
    res.status(200).render('Contact_us');
});
app.get('/StudentLogin', (req, res)=>{
    res.status(200).render('StudentLogin');
});


// Listening to connections
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});