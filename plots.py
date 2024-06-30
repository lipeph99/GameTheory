import matplotlib.pyplot as plt

pl1 = [48.3, 49.3, 51.3, 54.6, 59.7, 59.8, 58.4, 63.4, 62.7, 69.6, 74.4, 74.9, 73.2, 66.7, 73.8, 74.6, 69, 68.2, 74.6, 78.9, 73.6, 64.8, 77.9, 83.1, 89.1, 89.5, 86.4, 89.6, 91.1, 93, 92, 89.4, 93.6, 93.1, 91.2, 90.2, 92.1, 88.5, 84.2, 88.1, 90, 82.7, 83.5, 86.8, 83.5, 86.9, 90.1, 93.4, 89.7, 89.4, 93.2, 90.4, 87.2, 90, 93.1, 91.1, 89.4, 87.9, 88.8, 93, 90.9, 89.5, 92.5, 93.6, 93.1, 95, 93.6, 91.5, 93.4, 95, 93.4, 92.5, 92.6, 92.5, 92.1, 93, 91.7, 86.8, 84, 86.6, 83.6, 89.5, 89.9, 93.4, 91.9, 86.3, 86.7, 91.2, 89.9, 89.6, 90.9, 95.3, 96.5, 92.4, 91.1, 94.1, 94.5, 90.9, 92.3, 92.3]
pl2 = [50.8, 47.4, 42.5, 43.3, 54.1, 49.3, 51, 46.3, 47.4, 40.4, 36.5, 35.2, 30.6, 25.9, 26.7, 24.9, 31.8, 35, 35.8, 19.8, 18.8, 20.5, 25.2, 26.7, 22.4, 25.4, 23, 24.3, 25.4, 22.7, 23.6, 17.1, 16.5, 20.3, 22.4, 30.7, 19.6, 13.8, 13.5, 12.8, 14.9, 14.5, 13.9, 19.1, 14.3, 23.8, 29.3, 11.7, 15.2, 15.5, 16.3, 11.8, 15.3, 18, 15.9, 11.5, 7.5, 7.6, 9.8, 10.2, 12.8, 10.7, 12.2, 12.6, 13.9, 15, 12.2, 16.3, 17.1, 13.2, 12.4, 14.1, 12.9, 10.1, 8.6, 11.7, 11.8, 9.9, 17.8, 19, 16.8, 11.4, 9.9, 10, 12.8, 13.8, 15.3, 15.7, 13.6, 11.5, 13.6, 14.6, 16.5, 14.8, 13.9, 15.1, 8.7, 10.3, 11.4, 10.6]
pl3 = [51.57, 50.65, 52.62, 51.92, 55.37, 58.89, 57.67, 54.81, 49.26, 56.25, 63.17, 64.98, 71.25, 71.27, 73.65, 73.94, 77.07, 77.29, 80.55, 77.41, 81.23, 82.37, 79.97, 81.78, 82.69, 84.18, 84.02, 81.49, 81.06, 83.34, 82.23, 84.66, 84.41, 84.74, 86.90, 87.41, 83.34, 84.24, 84.22, 84.40, 84.99, 86.05, 85.98, 86.26, 84.40, 81.92, 82.31, 83.91, 83.98, 84.52, 83.15, 82.74, 81.06, 82.09, 83.63, 84.20, 83.85, 84.66, 82.74, 83.42, 84.56, 81.49, 82.64, 81.14, 78.13, 77.50, 79.20, 79.48, 81.72, 82.01, 83.69, 82.22, 83.89, 84.84, 83.29, 80.70, 80.11, 82.07, 81.11, 81.21, 81.84, 82.98, 82.19, 83.34, 82.25, 82.28, 82.60, 84.85, 86.02, 86.52, 86.76, 85.33, 85.12, 85.81, 86.55, 87.34, 86.74, 88.51, 88.24, 85.88]
pl4 = [49.32, 50.96, 57.25, 62.32, 53.33, 55.35, 48.37, 43.89, 44.45, 40.33, 33.38, 32.88, 31.23, 32.78, 33.47, 36.29, 35.23, 38.59, 41.49, 44.81, 47.59, 51.77, 49.09, 53.36, 53.62, 54.84, 60.29, 57.46, 51.72, 49.11, 49.38, 51.66, 51.33, 57.10, 56.45, 54.89, 57.88, 53.97, 54.08, 54.73, 55.88, 56.98, 57.13, 53.02, 51.49, 52.27, 54.14, 62.23, 63.61, 60.04, 59.47, 60.99, 58.49, 60.05, 61.66, 58.99, 59.02, 54.85, 56.49, 57.27, 62.49, 57.81, 61.31, 58.47, 59.24, 60.71, 58.53, 53.20, 47.70, 41.26, 40.14, 34.22, 42.73, 40.40, 45.80, 41.92, 44.80, 41.90, 40.59, 48.63, 52.73, 48.81, 46.92, 44.08, 44.06, 45.90, 46.14, 55.66, 54.60, 58.16, 58.04, 61.62, 58.92, 62.93, 54.98, 56.05, 50.09, 51.74, 53.33, 47.68]

plt.plot(pl1, 'blue')
plt.plot(pl2, 'blue')
plt.plot(pl4, 'red')
plt.ylabel('atkChance')
plt.xlabel('Gen')
plt.title("10 rounds fight")
plt.show()