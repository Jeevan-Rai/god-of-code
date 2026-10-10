// Day 01 — width is the whole difference between Rust and Python here.
// Run:  rustc rust/day01/main.rs -o /tmp/day01 && /tmp/day01

fn main() {
    let a: u8 = 0b1011_1010;

    println!("a                 = {:#010b}  ({})", a, a);
    println!("count_ones()      = {}", a.count_ones());
    println!("leading_zeros()   = {}", a.leading_zeros());
    println!("trailing_zeros()  = {}", a.trailing_zeros());
    println!("a << 3            = {:#010b}  (bits lost)", a << 3);
    println!("a.rotate_left(3)  = {:#010b}  (bits wrap)", a.rotate_left(3));
    println!("!a                = {:#010b}  ({})", !a, !a);
    println!();
    println!("0x1234u16 to_le   = {:02x?}", 0x1234u16.to_le_bytes());
    println!("0x1234u16 to_be   = {:02x?}", 0x1234u16.to_be_bytes());
    println!();
    println!("size_of::<u8>()   = {}", std::mem::size_of::<u8>());
    println!("size_of::<u64>()  = {}", std::mem::size_of::<u64>());
    println!("size_of::<usize>()= {}", std::mem::size_of::<usize>());
}
