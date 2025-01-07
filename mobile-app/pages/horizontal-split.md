# Background
<v-switch transition="fade">
  <template #0>
    <div class="grid grid-rows-[25%_80%] gap-4 h-3/4">
      <!-- First Row -->
      <div>
        <div class="grid grid-cols-[50%_50%] gap-4">
          <!-- First col -->
          <div>
            <p><strong>Declarative Design</strong></p>
            <ul>
              <li>Container images</li>
              <li>Deployment configurations</li>
            </ul>
          </div>
          <div>
            <p><strong>Platform independent</strong></p>
            <ul>
              <li>Containers are dependent on Linux</li>
              <li>Components can run everywhere</li>
            </ul>
          </div>
        </div>
      </div>
      <!-- Second Row -->
      <div>
        <img src="/cloud-history.jpeg" alt="heh" class="h-[90%] w-auto block mx-auto">
      </div>
    </div>
  </template>
  <template #1>
    <div class="grid grid-rows-[50%_50%] gap-8">
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
  </template>
</v-switch>

<Footer />

<style>
p {
  margin-top: 0rem;
  margin-bottom: 0rem;
}
</style>
