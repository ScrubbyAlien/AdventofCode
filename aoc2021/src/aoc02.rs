use std::fs;

fn parse() -> Vec<String> {
    let filename = "inputs/input02.txt";
    let content = fs::read_to_string(filename).unwrap();

    return content.trim().split('\n').map(|s| s.to_string()).collect();
}

pub fn part1() {
    let list: Vec<_> = parse();

    let mut res_vec = vec![0, 0];

    for elem in list {
        let vec: Vec<_> = elem.split(' ').collect();

        let instr = vec[0];
        let value = vec[1].parse::<i32>().unwrap();

        if instr == "forward" {
            res_vec[0] = res_vec[0] + value;
        }

        if instr == "down" {
            res_vec[1] = res_vec[1] + value;
        }

        if instr == "up" {
            res_vec[1] = res_vec[1] - value;
        }
    }

    println!("2021 02 part 1: {:?}", res_vec[0] * res_vec[1]);
}

pub fn part2() {
    let list: Vec<_> = parse();

    let mut res_vec = vec![0, 0, 0];

    for elem in list {
        let vec: Vec<_> = elem.split(' ').collect();

        let instr = vec[0];
        let value = vec[1].parse::<i32>().unwrap();

        if instr == "forward" {
            res_vec[0] = res_vec[0] + value;
            res_vec[1] = res_vec[1] + (res_vec[2] * value);
        }

        if instr == "down" {
            res_vec[2] = res_vec[2] + value;
        }

        if instr == "up" {
            res_vec[2] = res_vec[2] - value;
        }
    }

    println!("2021 02 part 2: {:?}", res_vec[0] * res_vec[1]);
}
