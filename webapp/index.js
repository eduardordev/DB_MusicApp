const { Pool } = requiere ('pg');

const config = {
	user: 'postgres',
	host: 'localhost',
	password: ' ',
	database: 'library'
};

const pool = new Pool (config);

const getMusic = async () => {
	try {
		const res = await pool.querty ('select * from music')
		console.log(res.rows)
		pool.end();
	} catch(e) {
		console.log(e);
	}
};
/*
const insertUser = async () => {
	try{
	const text = 'INSERT INTO users(username, password) VALUES($1, $2)'
	const values = ['john' , 'john1234']
	
	const res = await pool.querty(text, values);
	console.log(res);
	pool.end();
	}catch(e){
		console.log(e);

	}
	
	

}
const deleteUser = async () => {
	const text = 'DELETE FROM users WHERE username = $1';
	const value = ['john'];

	const res = await pool.query(text, value);
	console.log (res)
}


const editUser = async () => {
	const text = 'UPDATE users SET username = $1 WHERE username = $2';
	const values = ['John', 'ryan'];

	const res = await pool.query(text, values);
	console.log(res);

};

editUser();
//deleteUser();
*/
getMusic();
