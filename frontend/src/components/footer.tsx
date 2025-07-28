import React from 'react';
import '../styles/footer.css';


const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="footer_content">
        <p>&copy; {new Date().getFullYear()} Herugil. KrzakalaPaul. Lulu. Uporito. All rights reserved.</p>
        <div className="footer_links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Contact</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
