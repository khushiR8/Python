const canvas = document.getElementById('fireworks');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

function random(min, max) {
  return Math.random() * (max - min) + min;
}

class Particle {
  constructor(x, y, angle, speed, color) {
    this.x = x;
    this.y = y;
    this.angle = angle;
    this.speed = speed;
    this.color = color;
    this.life = 100;
    this.alpha = 1;
  }

  update() {
    const gravity = 0.02;
    this.x += Math.cos(this.angle) * this.speed;
    this.y += Math.sin(this.angle) * this.speed + gravity;
    this.speed *= 0.98;
    this.life--;
    this.alpha = this.life / 100;
  }

  draw() {
    ctx.save();
    ctx.globalAlpha = this.alpha;
    ctx.beginPath();
    ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.restore();
  }
}

let particles = [];

function createFirework(x, y) {
  const color = `hsl(${Math.random() * 360}, 100%, 70%)`;
  for (let i = 0; i < 80; i++) {
    const angle = (Math.PI * 2 * i) / 80;
    const speed = random(2, 5);
    particles.push(new Particle(x, y, angle, speed, color));
  }
}

function animate() {
    requestAnimationFrame(animate);
  
    // Clear canvas without painting over the background
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    if (Math.random() < 0.04) {
      const x = random(canvas.width * 0.2, canvas.width * 0.8);
      const y = random(canvas.height * 0.1, canvas.height * 0.6);
      createFirework(x, y);
    }
  
    particles.forEach((p, i) => {
      p.update();
      p.draw();
      if (p.life <= 0) particles.splice(i, 1);
    });
  }
  

animate();