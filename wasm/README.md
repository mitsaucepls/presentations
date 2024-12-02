# Welcome to [Slidev](https://github.com/slidevjs/slidev)!

To start the slide show:

- `npm install`
- `npm run dev`
- visit <http://localhost:3030>

Edit the [slides.md](./slides.md) to see the changes.

Learn more about Slidev at the [documentation](https://sli.dev/).

Bevy workflow:
```rust
App::new()
    .add_plugins(DefaultPlugins.set(WindowPlugin {
        primary_window: Some(Window {
            fit_canvas_to_parent: true,
            canvas: Some("#game-canvas".into()), //references the id of the canvas element
            ..default()
        }),
        ..default()
    }))
    //...
    .run();
```
```bash
cargo build --release --example animated_transform --target wasm32-unknown-unknown
```
```bash
wasm-bindgen --out-name animated_transform --out-dir ../components/target/ --target web target/wasm32-unknown-unknown/release/examples/animated_transform.wasm
```

washed up workflow:
```bash
wash up
```
