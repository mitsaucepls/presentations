<div class="h-full flex flex-col">

# Hard-Skills
<div class="flex flex-1 flex-col mb-14">
<div class="grid grid-cols-[50%_50%] gap-4" style="height: 60%">
  <!-- First column -->
  <div class="vertical-center">
    <div>
      <div>
        <p><strong>Skills</strong></p>
        <ul style="padding-left: 20px;">
          <li>Linux
            <ul class="dash-list">
              <li>Main OS, Terminal Based Workflow</li>
            </ul>
          </li>
          <li>Orchestration
            <ul class="dash-list">
              <li>
                Docker, Kubernetes, Helm, Kustomize
              </li>
            </ul>
          </li>
          <li>Programming
            <ul class="dash-list">
              <li>Rust, Python, Java, Typescript</li>
            </ul>
          </li>
          <li>Datenbanken
            <ul class="dash-list">
              <li>PostgreSQL, MongoDB</li>
            </ul>
          </li>
          <li>CI/CD
            <ul class="dash-list">
              <li>GitOps, GitLabCI/CD, ArgoCD</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- Second column -->
  <div class="vertical-center-img">
    <div>
      <img src="/dev-ops.png" alt="heh" width="100%" height="100%" class="center">
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
.vertical-center {
  display: block;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.vertical-center-img {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
ul.dash-list li::before {
  content: "- ";
}
ul.dash-list {
  list-style-type: none; /* Remove default bullet points */
}
</style>
