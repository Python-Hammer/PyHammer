import React from 'react';
import '../styles/card.css';

type CardProps = {
  title: string;
  content: string;
};

const SimpleCard: React.FC<CardProps> = ({ title, content }) => {
  return (
    <div className='card'>
      <h3 className='card__title'>{title}</h3>
      <p className='card__content'>{content}</p>
    </div>
  );
};

export default SimpleCard;
