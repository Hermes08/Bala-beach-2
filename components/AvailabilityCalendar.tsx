
import React, { useState, useEffect } from 'react';
import { ChevronLeft, ChevronRight, Calendar as CalendarIcon, AlertCircle } from 'lucide-react';
import { Language } from '../types';
import { CONTENT, AIRBNB_ICAL_URL } from '../constants';

interface Props {
  lang: Language;
}

const AvailabilityCalendar: React.FC<Props> = ({ lang }) => {
  const t = CONTENT[lang].calendar;
  const [currentDate, setCurrentDate] = useState(new Date());
  const [bookedDates, setBookedDates] = useState<Date[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const fetchCalendar = async () => {
      try {
        // Using a CORS proxy to bypass browser restrictions
        const proxyUrl = `https://corsproxy.io/?${encodeURIComponent(AIRBNB_ICAL_URL)}`;
        const response = await fetch(proxyUrl);
        
        if (!response.ok) throw new Error('Failed to fetch calendar');
        
        const data = await response.text();
        parseICal(data);
      } catch (err) {
        console.error('Error fetching calendar:', err);
        setError(true);
      } finally {
        setLoading(false);
      }
    };

    fetchCalendar();
  }, []);

  const parseICal = (data: string) => {
    const dates: Date[] = [];
    // Simple Regex to find event start and end dates
    // Format: DTSTART;VALUE=DATE:20250218
    const eventRegex = /BEGIN:VEVENT[\s\S]*?DTSTART;VALUE=DATE:(\d{8})[\s\S]*?DTEND;VALUE=DATE:(\d{8})[\s\S]*?END:VEVENT/g;
    
    let match;
    while ((match = eventRegex.exec(data)) !== null) {
      const startStr = match[1]; // e.g. 20250218
      const endStr = match[2];   // e.g. 20250220
      
      const start = new Date(
        parseInt(startStr.substring(0, 4)),
        parseInt(startStr.substring(4, 6)) - 1,
        parseInt(startStr.substring(6, 8))
      );
      
      const end = new Date(
        parseInt(endStr.substring(0, 4)),
        parseInt(endStr.substring(4, 6)) - 1,
        parseInt(endStr.substring(6, 8))
      );

      // Loop through dates between start (inclusive) and end (exclusive)
      for (let dt = new Date(start); dt < end; dt.setDate(dt.getDate() + 1)) {
        dates.push(new Date(dt));
      }
    }
    setBookedDates(dates);
  };

  const isDateBooked = (date: Date) => {
    return bookedDates.some(
      booked => 
        booked.getDate() === date.getDate() &&
        booked.getMonth() === date.getMonth() &&
        booked.getFullYear() === date.getFullYear()
    );
  };

  const getDaysInMonth = (date: Date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    
    const days = [];
    // Empty slots for days before the 1st
    for (let i = 0; i < firstDayOfMonth; i++) {
      days.push(null);
    }
    // Days of the month
    for (let i = 1; i <= daysInMonth; i++) {
      days.push(new Date(year, month, i));
    }
    return days;
  };

  const nextMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1));
  };

  const prevMonth = () => {
    setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1));
  };

  const days = getDaysInMonth(currentDate);
  const monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];

  return (
    <div className="bg-white rounded-3xl shadow-xl overflow-hidden border border-brand-100 max-w-4xl mx-auto">
      <div className="bg-brand-900 p-6 text-white text-center">
        <h3 className="font-serif text-2xl font-bold mb-2 flex items-center justify-center gap-2">
          <CalendarIcon size={24} /> {t.title}
        </h3>
        <p className="text-brand-100 text-sm">{t.subtitle}</p>
      </div>

      <div className="p-6 md:p-10">
        {error ? (
          <div className="text-center py-10">
            <div className="text-red-500 mb-4 flex justify-center"><AlertCircle size={48} /></div>
            <p className="text-slate-600 mb-6">{t.error}</p>
            <a 
              href="https://www.airbnb.com/rooms/1409650618945019706" 
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-brand-500 text-white px-6 py-3 rounded-full font-bold hover:bg-brand-600 transition-colors"
            >
              {t.checkButton}
            </a>
          </div>
        ) : (
          <>
            {/* Controls */}
            <div className="flex justify-between items-center mb-8">
              <button onClick={prevMonth} className="p-2 hover:bg-slate-100 rounded-full transition-colors text-slate-600">
                <ChevronLeft size={24} />
              </button>
              <h4 className="text-xl font-bold text-slate-800">
                {monthNames[currentDate.getMonth()]} {currentDate.getFullYear()}
              </h4>
              <button onClick={nextMonth} className="p-2 hover:bg-slate-100 rounded-full transition-colors text-slate-600">
                <ChevronRight size={24} />
              </button>
            </div>

            {/* Calendar Grid */}
            <div className="grid grid-cols-7 gap-2 mb-6">
              {['S', 'M', 'T', 'W', 'T', 'F', 'S'].map((day, i) => (
                <div key={i} className="text-center text-xs font-bold text-slate-400 uppercase tracking-wide">
                  {day}
                </div>
              ))}
              
              {loading ? (
                // Loading Skeleton
                [...Array(35)].map((_, i) => (
                  <div key={i} className="aspect-square bg-slate-100 animate-pulse rounded-lg"></div>
                ))
              ) : (
                days.map((date, index) => {
                  if (!date) return <div key={index} className="aspect-square"></div>;
                  
                  const isBooked = isDateBooked(date);
                  const isPast = date < new Date(new Date().setHours(0,0,0,0));
                  
                  return (
                    <div 
                      key={index}
                      className={`
                        aspect-square flex items-center justify-center text-sm font-medium rounded-lg transition-all
                        ${isPast 
                          ? 'text-slate-300 cursor-not-allowed' 
                          : isBooked 
                            ? 'bg-slate-100 text-slate-400 line-through cursor-not-allowed' 
                            : 'bg-green-50 text-green-700 hover:bg-green-100 cursor-pointer border border-green-100 shadow-sm'
                        }
                      `}
                    >
                      {date.getDate()}
                    </div>
                  );
                })
              )}
            </div>

            {/* Legend */}
            <div className="flex justify-center gap-6 text-sm">
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
                <span className="text-slate-600">{t.available}</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full bg-slate-300"></div>
                <span className="text-slate-600">{t.booked}</span>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default AvailabilityCalendar;
