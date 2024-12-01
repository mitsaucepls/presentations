---
hideInToc: true
---
<div class="h-full flex flex-col">

  # Environment
  <div class="flex flex-1 flex-col mb-14">
    <div class="grid grid-rows-[50%_50%] gap-4 h-full">
      <!-- First Row -->
      <div>
        <div class="grid grid-cols-[50%_50%] gap-4">
          <!-- First col -->
          <div>
            <p><strong>⚙ Compilers</strong></p>
            <ul>
              <li>Binaryen (wasm-opt)</li>
              <li>rustc (standard Rust compiler)</li>
              <li>TinyGo (lightweight Go compiler)</li>
            </ul>
          </div>
          <!-- Second col -->
          <div>
            <p><strong>🛡️ Security</strong></p>
            <ul>
              <li>Sandboxing & WASI</li>
              <li>Control-Flow Integrity</li>
              <li>Memory Safety</li>
            </ul>
          </div>
        </div>
      </div>
      <!-- Second Row -->
      <div>
        <div class="grid grid-cols-[50%_50%] gap-4">
          <!-- First col -->
          <div>
            <p><strong>⏳ Runtimes</strong></p>
            <ul>
              <li>Wasmer (cross-platform)</li>
              <li>Node.js (cross-platform)</li>
              <li>Wasmtime (cross-platform)</li>
            </ul>
          </div>
          <!-- Second col -->
          <div>
            <p><strong>🛠 Tools and Platforms</strong></p>
            <ul>
              <li>WABT (wasm2wat, wasm2c, wasm-stats)</li>
              <li>wit-bindgen, wit-deps, and wai</li>
              <li>WasmCloud, Fermyon Spin, SpiderLightning</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<Footer />

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
p {
  margin-top: 1rem;
  margin-bottom: 0rem;
}
</style>
