use std::fs;


pub fn foobar() {
    let filename = "inputs/input01.txt";
    let contents = fs::read_to_string(filename).unwrap();

    let list: Vec<_> = contents.trim().split('\n').collect();

    let mut sum = 0;

    for elem in list {
        let num: f32 = elem.parse().unwrap();

        sum = sum + (num/3.0).floor() as i32 - 2;
    }

    println!("{}", sum);
}