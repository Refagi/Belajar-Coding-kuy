//rumus mencari angka random dengan batas
// let max = 10
// let min = 1
// let result = Math.floor(Math.random() * (max - min + 1)) + min
// alert(result)


// for (;;){
    let musuh = Math.random()
    let pelayer = prompt('masukan karakter:\nsemut, orang atau gajah')
    let result = ''
    // alert(musuh)
    for (let i = 0; i < musuh; i++){
        if (musuh < 0.40){
            musuh = 'semut'
        } else if (musuh >= 0.40 && musuh <= 0.60){
            musuh = 'orang'
        } else {
            musuh = 'gajah'
        }

        if (pelayer === musuh){
            result = 'wah kamu seri'
        } else if (pelayer === 'orang'){
            if (musuh === 'semut'){
                result = 'yey kamu menang'
            }
        } else if (pelayer === 'gajah'){
            if (musuh === 'orang'){
                result = 'yey kamu menang'
            }
        } else if (pelayer === 'semut'){
            if (musuh === 'orang' || musuh === 'gajah'){
                result = 'yah kamu kalah'
            }
        }
        alert(`kamu pilih ${pelayer} dan musuh pilih ${musuh}`)
        alert(result)
    }
// }

